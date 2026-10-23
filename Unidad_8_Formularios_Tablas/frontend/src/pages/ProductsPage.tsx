import { useState, useMemo } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import {
  flexRender,
  getCoreRowModel,
  getPaginationRowModel,
  getSortedRowModel,
  useReactTable,
  createColumnHelper,
  type PaginationState,
  type SortingState,
} from '@tanstack/react-table';
import {
  getProductos,
  createProducto,
  updateProducto,
  deleteProducto,
} from '../services/producto';
import type { Producto } from '../types/producto';
import ProductoModal from '../components/ProductoModal';
import TablePagination from '../components/TablePagination';

const columnHelper = createColumnHelper<Producto>();

export default function ProductsPage() {
  const queryClient = useQueryClient();

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [productoEditar, setProductoEditar] = useState<Producto | null>(null);
  const [modalError, setModalError] = useState<string | null>(null);

  const [sorting, setSorting] = useState<SortingState>([]);
  const [pagination, setPagination] = useState<PaginationState>({
    pageIndex: 0,
    pageSize: 5,
  });

  const {
    data: productos = [],
    isLoading,
    isError,
    error,
    refetch,
  } = useQuery({
    queryKey: ['productos'],
    queryFn: getProductos,
  });

  const createMutation = useMutation({
    mutationFn: createProducto,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['productos'] });
      handleCloseModal();
    },
    onError: (err: Error) => setModalError(err.message),
  });

  const updateMutation = useMutation({
    mutationFn: updateProducto,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['productos'] });
      handleCloseModal();
    },
    onError: (err: Error) => setModalError(err.message),
  });

  const deleteMutation = useMutation({
    mutationFn: deleteProducto,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['productos'] });
    },
    onError: (err: Error) => alert(`Error al eliminar: ${err.message}`),
  });

  const handleOpenCreate = () => {
    setProductoEditar(null);
    setModalError(null);
    setIsModalOpen(true);
  };

  const handleOpenEdit = (producto: Producto) => {
    setProductoEditar(producto);
    setModalError(null);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setProductoEditar(null);
    setModalError(null);
  };

  const handleSubmitModal = (data: {
    nombre: string;
    descripcion: string;
    precio_base: number;
    disponible: boolean;
  }) => {
    setModalError(null);
    if (productoEditar) {
      updateMutation.mutate({ id: productoEditar.id, data });
    } else {
      createMutation.mutate(data);
    }
  };

  const handleDelete = (id: number) => {
    if (window.confirm('?Seguro que deseas eliminar este producto?')) {
      deleteMutation.mutate(id);
    }
  };

  const columns = useMemo(
    () => [
      columnHelper.accessor('id', {
        header: 'ID',
        cell: (info) => (
          <span className="px-2 py-0.5 rounded-md bg-teal-500/10 text-teal-400 font-mono text-xs border border-teal-500/20">
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
              {{ asc: ' ?', desc: ' ?' }[column.getIsSorted() as string] ?? ' ?'}
            </span>
          </button>
        ),
        cell: (info) => <span className="font-semibold text-white">{info.getValue()}</span>,
      }),
      columnHelper.accessor('descripcion', {
        header: 'Descripci?n',
        cell: (info) => (
          <span className="text-slate-300 text-sm max-w-xs truncate block">
            {info.getValue() || <span className="text-slate-500 italic">Sin descripci?n</span>}
          </span>
        ),
      }),
      columnHelper.accessor('precio_base', {
        header: ({ column }) => (
          <button
            onClick={column.getToggleSortingHandler()}
            className="flex items-center gap-1 font-semibold text-slate-200 hover:text-white cursor-pointer"
          >
            <span>Precio</span>
            <span className="text-xs">
              {{ asc: ' ?', desc: ' ?' }[column.getIsSorted() as string] ?? ' ?'}
            </span>
          </button>
        ),
        cell: (info) => (
          <span className="font-mono text-emerald-400 font-semibold">
            ${Number(info.getValue()).toLocaleString('es-AR', { minimumFractionDigits: 2 })}
          </span>
        ),
      }),
      columnHelper.accessor('disponible', {
        header: 'Estado',
        cell: (info) => (
          <span
            className={`px-2 py-1 rounded-full text-xs font-semibold ${
              info.getValue()
                ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/20'
                : 'bg-rose-500/10 text-rose-400 border border-rose-500/20'
            }`}
          >
            {info.getValue() ? 'Disponible' : 'Agotado'}
          </span>
        ),
      }),
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
      }),
    ],
    []
  );

  const table = useReactTable({
    data: productos,
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
              Gesti?n de Productos
            </h1>
            <span className="px-3 py-1 rounded-full text-xs font-semibold bg-teal-500/10 text-teal-400 border border-teal-500/20">
              CRUD Completo
            </span>
          </div>
          <p className="mt-1 text-sm text-slate-400">
            Administraci?n del cat?logo con TanStack Table v8 y TanStack Form.
          </p>
        </div>

        <button
          onClick={handleOpenCreate}
          className="px-5 py-2.5 rounded-xl font-semibold text-white bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-600 hover:to-teal-600 shadow-lg shadow-emerald-500/20 transition-all flex items-center justify-center gap-2 cursor-pointer"
        >
          <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
          </svg>
          Nuevo producto
        </button>
      </div>

      {isLoading ? (
        <div className="bg-slate-800/40 border border-slate-700/60 rounded-3xl p-8 animate-pulse space-y-4">
          <div className="h-6 bg-slate-700 rounded w-1/4" />
          <div className="h-10 bg-slate-700/60 rounded w-full" />
          <div className="h-10 bg-slate-700/60 rounded w-full" />
        </div>
      ) : isError ? (
        <div className="p-6 rounded-2xl bg-rose-500/10 border border-rose-500/30 text-center max-w-lg mx-auto">
          <h3 className="text-lg font-bold text-white mb-1">Error al cargar productos</h3>
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
      ) : productos.length === 0 ? (
        <div className="text-center py-16 px-4 bg-slate-800/40 border border-dashed border-slate-700 rounded-3xl">
          <h3 className="text-lg font-semibold text-slate-200 mb-1">No hay productos registrados</h3>
          <p className="text-sm text-slate-400 mb-4">
            Comienza creando el primer producto del cat?logo.
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

      <ProductoModal
        isOpen={isModalOpen}
        onClose={handleCloseModal}
        onSubmit={handleSubmitModal}
        productoEditar={productoEditar}
        isLoading={isSubmitting}
        errorMessage={modalError}
      />
    </div>
  );
}
