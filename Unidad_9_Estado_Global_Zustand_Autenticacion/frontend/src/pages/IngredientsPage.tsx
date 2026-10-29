import { useState, useMemo } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import {
  flexRender,
  getCoreRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
  createColumnHelper,
  type ColumnDef,
  type PaginationState,
  type SortingState,
} from '@tanstack/react-table';
import {
  getIngredientes,
  createIngrediente,
  updateIngrediente,
  deleteIngrediente,
} from '../services/ingrediente.service';
import type { Ingrediente } from '../types/ingrediente';
import IngredienteModal from '../components/IngredienteModal';
import TablePagination from '../components/TablePagination';
import { useAuthStore } from '../store/authStore';

const columnHelper = createColumnHelper<Ingrediente>();

export default function IngredientsPage() {
  const queryClient = useQueryClient();
  const { user } = useAuthStore();
  const isAdmin = user?.role === 'admin';

  // Estados locales UI
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [ingredienteEditar, setIngredienteEditar] = useState<Ingrediente | null>(null);
  const [modalError, setModalError] = useState<string | null>(null);

  // Estados de TanStack Table
  const [sorting, setSorting] = useState<SortingState>([]);
  const [pagination, setPagination] = useState<PaginationState>({
    pageIndex: 0,
    pageSize: 5,
  });

  // Server State con TanStack Query
  const {
    data: ingredientes = [],
    isLoading,
    isError,
    error,
    refetch,
  } = useQuery({
    queryKey: ['ingredientes'],
    queryFn: getIngredientes,
  });

  // Mutaciones
  const createMutation = useMutation({
    mutationFn: createIngrediente,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['ingredientes'] });
      handleCloseModal();
    },
    onError: (err: any) =>
      setModalError(err.response?.data?.detail || err.message || 'Error al crear ingrediente'),
  });

  const updateMutation = useMutation({
    mutationFn: updateIngrediente,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['ingredientes'] });
      handleCloseModal();
    },
    onError: (err: any) =>
      setModalError(err.response?.data?.detail || err.message || 'Error al actualizar ingrediente'),
  });

  const deleteMutation = useMutation({
    mutationFn: deleteIngrediente,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['ingredientes'] });
    },
    onError: (err: any) =>
      alert(`Error al eliminar: ${err.response?.data?.detail || err.message}`),
  });

  const handleOpenCreate = () => {
    setIngredienteEditar(null);
    setModalError(null);
    setIsModalOpen(true);
  };

  const handleOpenEdit = (ingrediente: Ingrediente) => {
    setIngredienteEditar(ingrediente);
    setModalError(null);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setIngredienteEditar(null);
    setModalError(null);
  };

  const handleSubmitModal = (data: { nombre: string }) => {
    setModalError(null);
    if (ingredienteEditar) {
      updateMutation.mutate({ id: ingredienteEditar.id, data });
    } else {
      createMutation.mutate(data);
    }
  };

  const handleDelete = (id: number) => {
    if (window.confirm('¿Seguro que deseas eliminar este ingrediente?')) {
      deleteMutation.mutate(id);
    }
  };

  // Definición de Columnas para TanStack Table (condicional según rol admin, HU-05)
  const columns = useMemo(() => {
    const baseCols: ColumnDef<Ingrediente, any>[] = [
      columnHelper.accessor('id', {
        header: 'ID',
        cell: (info) => (
          <span className="px-2 py-0.5 rounded-md bg-purple-500/10 text-purple-400 font-mono text-xs border border-purple-500/20">
            #{info.getValue()}
          </span>
        ),
      }),
      columnHelper.accessor('nombre', {
        header: ({ column }) => (
          <button
            onClick={column.getToggleSortingHandler()}
            className="flex items-center gap-1 font-semibold text-slate-200 hover:text-white cursor-pointer"
          >
            <span>Nombre</span>
            <span className="text-xs">
              {{ asc: ' 🔼', desc: ' 🔽' }[column.getIsSorted() as string] ?? ' ↕'}
            </span>
          </button>
        ),
        cell: (info) => <span className="font-semibold text-white">{info.getValue()}</span>,
      }),
    ];

    if (isAdmin) {
      baseCols.push(
        columnHelper.display({
          id: 'acciones',
          header: () => <span className="text-right block">Acciones</span>,
          cell: ({ row }) => (
            <div className="flex items-center justify-end gap-2">
              <button
                onClick={() => handleOpenEdit(row.original)}
                className="px-2.5 py-1.5 rounded-lg text-xs font-medium bg-slate-700/60 hover:bg-slate-700 text-slate-200 hover:text-white transition-colors cursor-pointer"
              >
                Editar
              </button>
              <button
                onClick={() => handleDelete(row.original.id)}
                className="px-2.5 py-1.5 rounded-lg text-xs font-medium bg-rose-500/10 hover:bg-rose-500/20 text-rose-300 hover:text-rose-200 border border-rose-500/20 transition-colors cursor-pointer"
              >
                Eliminar
              </button>
            </div>
          ),
        })
      );
    }

    return baseCols;
  }, [isAdmin]);

  const table = useReactTable({
    data: ingredientes,
    columns,
    state: { sorting, pagination },
    onSortingChange: setSorting,
    onPaginationChange: setPagination,
    getCoreRowModel: getCoreRowModel(),
    getSortedRowModel: getSortedRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
  });

  const isSubmitting = createMutation.isPending || updateMutation.isPending;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 pb-8 mb-8 border-b border-slate-800">
        <div>
          <div className="flex items-center gap-3">
            <h1 className="text-3xl font-extrabold text-white tracking-tight">
              Gestión de Ingredientes
            </h1>
            <span className="px-3 py-1 rounded-full text-xs font-semibold bg-purple-500/10 text-purple-400 border border-purple-500/20">
              TanStack Table &amp; Form
            </span>
          </div>
          <p className="mt-1 text-sm text-slate-400">
            Catálogo de ingredientes para recetas. {isAdmin ? 'Tienes permisos de Administrador para crear, editar y eliminar.' : 'Modo sólo lectura (Rol Usuario).'}
          </p>
        </div>

        {isAdmin && (
          <button
            onClick={handleOpenCreate}
            className="px-5 py-2.5 rounded-xl font-semibold text-white bg-gradient-to-r from-purple-500 to-indigo-500 hover:from-purple-600 hover:to-indigo-600 shadow-lg shadow-purple-500/20 transition-all flex items-center justify-center gap-2 cursor-pointer"
          >
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
            </svg>
            Nuevo ingrediente
          </button>
        )}
      </div>

      {isLoading ? (
        <div className="bg-slate-800/40 border border-slate-700/60 rounded-3xl p-8 animate-pulse space-y-4">
          <div className="h-6 bg-slate-700 rounded w-1/4" />
          <div className="h-10 bg-slate-700/60 rounded w-full" />
        </div>
      ) : isError ? (
        <div className="p-6 rounded-2xl bg-rose-500/10 border border-rose-500/30 text-center max-w-lg mx-auto">
          <h3 className="text-lg font-bold text-white mb-1">Error al cargar ingredientes</h3>
          <p className="text-sm text-rose-300 mb-4">
            {error instanceof Error ? error.message : 'No se pudo conectar con el servidor'}
          </p>
          <button
            onClick={() => refetch()}
            className="px-4 py-2 rounded-xl text-sm font-semibold bg-rose-500 text-white hover:bg-rose-600 transition-colors"
          >
            Reintentar
          </button>
        </div>
      ) : ingredientes.length === 0 ? (
        <div className="text-center py-16 px-4 bg-slate-800/40 border border-dashed border-slate-700 rounded-3xl">
          <h3 className="text-lg font-semibold text-slate-200 mb-1">No hay ingredientes registrados</h3>
          <p className="text-sm text-slate-400 mb-4">
            {isAdmin ? 'Haz clic en "Nuevo ingrediente" para registrar el primero.' : 'Actualmente no hay ingredientes disponibles.'}
          </p>
        </div>
      ) : (
        <div className="bg-slate-800/60 border border-slate-700 rounded-3xl overflow-hidden shadow-xl">
          <div className="overflow-x-auto">
            <table className="w-full text-left text-sm">
              <thead className="bg-slate-900/80 text-slate-300 border-b border-slate-700/80 text-xs uppercase tracking-wider">
                {table.getHeaderGroups().map((headerGroup) => (
                  <tr key={headerGroup.id}>
                    {headerGroup.headers.map((header) => (
                      <th key={header.id} className="py-4 px-6 font-semibold">
                        {header.isPlaceholder
                          ? null
                          : flexRender(header.column.columnDef.header, header.getContext())}
                      </th>
                    ))}
                  </tr>
                ))}
              </thead>
              <tbody className="divide-y divide-slate-700/60 text-slate-200">
                {table.getRowModel().rows.map((row) => (
                  <tr key={row.id} className="hover:bg-slate-700/30 transition-colors">
                    {row.getVisibleCells().map((cell) => (
                      <td key={cell.id} className="py-4 px-6">
                        {flexRender(cell.column.columnDef.cell, cell.getContext())}
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>

          <TablePagination table={table} />
        </div>
      )}

      {isAdmin && (
        <IngredienteModal
          isOpen={isModalOpen}
          onClose={handleCloseModal}
          onSubmit={handleSubmitModal}
          ingredienteEditar={ingredienteEditar}
          isLoading={isSubmitting}
          errorMessage={modalError}
        />
      )}
    </div>
  );
}
