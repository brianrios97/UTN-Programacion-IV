import { useState } from 'react';
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import {
  getCategorias,
  createCategoria,
  updateCategoria,
  deleteCategoria,
} from '../services/categoria';
import type { Categoria } from '../types/categoria';
import CategoriaList from '../components/CategoriaList';
import CategoriaModal from '../components/CategoriaModal';

export default function CategoriasPage() {
  const queryClient = useQueryClient();

  const [isModalOpen, setIsModalOpen] = useState(false);
  const [categoriaEditar, setCategoriaEditar] = useState<Categoria | null>(null);
  const [deletingId, setDeletingId] = useState<number | null>(null);
  const [modalError, setModalError] = useState<string | null>(null);

  const {
    data: categorias = [],
    isLoading,
    isError,
    error,
    refetch,
  } = useQuery({
    queryKey: ['categorias'],
    queryFn: getCategorias,
  });

  const createMutation = useMutation({
    mutationFn: createCategoria,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['categorias'] });
      handleCloseModal();
    },
    onError: (err: Error) => {
      setModalError(err.message);
    },
  });

  const updateMutation = useMutation({
    mutationFn: updateCategoria,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['categorias'] });
      handleCloseModal();
    },
    onError: (err: Error) => {
      setModalError(err.message);
    },
  });

  const deleteMutation = useMutation({
    mutationFn: deleteCategoria,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['categorias'] });
      setDeletingId(null);
    },
    onError: (err: Error) => {
      alert(`Error al eliminar: ${err.message}`);
      setDeletingId(null);
    },
  });

  const handleOpenCreateModal = () => {
    setCategoriaEditar(null);
    setModalError(null);
    setIsModalOpen(true);
  };

  const handleOpenEditModal = (categoria: Categoria) => {
    setCategoriaEditar(categoria);
    setModalError(null);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setCategoriaEditar(null);
    setModalError(null);
  };

  const handleSubmitModal = (data: { nombre: string; descripcion: string }) => {
    setModalError(null);
    if (categoriaEditar) {
      updateMutation.mutate({
        id: categoriaEditar.id,
        data,
      });
    } else {
      createMutation.mutate(data);
    }
  };

  const handleDelete = (id: number) => {
    if (window.confirm('?Est?s seguro de que deseas eliminar esta categor?a?')) {
      setDeletingId(id);
      deleteMutation.mutate(id);
    }
  };

  const isSubmitting = createMutation.isPending || updateMutation.isPending;

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4 pb-8 mb-8 border-b border-slate-800">
        <div>
          <div className="flex items-center gap-3">
            <h1 className="text-3xl font-extrabold text-white tracking-tight">
              Gesti?n de Categor?as
            </h1>
            <span className="px-3 py-1 rounded-full text-xs font-semibold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
              {categorias.length} {categorias.length === 1 ? 'categor?a' : 'categor?as'}
            </span>
          </div>
          <p className="mt-1 text-sm text-slate-400">
            CRUD completo sincronizado en tiempo real con FastAPI y TanStack Query.
          </p>
        </div>

        <button
          onClick={handleOpenCreateModal}
          className="px-5 py-2.5 rounded-xl font-semibold text-white bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-600 hover:to-teal-600 shadow-lg shadow-emerald-500/20 transition-all flex items-center justify-center gap-2 cursor-pointer"
        >
          <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
          </svg>
          Nueva Categor?a
        </button>
      </div>

      {isLoading ? (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {[1, 2, 3].map((n) => (
            <div key={n} className="bg-slate-800/40 border border-slate-700/50 rounded-2xl p-6 animate-pulse">
              <div className="h-4 bg-slate-700 rounded w-1/3 mb-4" />
              <div className="h-6 bg-slate-700 rounded w-3/4 mb-3" />
              <div className="h-4 bg-slate-700 rounded w-full mb-2" />
              <div className="h-4 bg-slate-700 rounded w-2/3 mb-6" />
              <div className="h-9 bg-slate-700 rounded w-full" />
            </div>
          ))}
        </div>
      ) : isError ? (
        <div className="p-6 rounded-2xl bg-rose-500/10 border border-rose-500/30 text-center max-w-lg mx-auto">
          <svg className="w-12 h-12 text-rose-400 mx-auto mb-3" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
          </svg>
          <h3 className="text-lg font-bold text-white mb-1">Error al conectar con el servidor</h3>
          <p className="text-sm text-rose-300 mb-4">
            {error instanceof Error ? error.message : 'No se pudo obtener el listado de categor?as.'}
          </p>
          <button
            onClick={() => refetch()}
            className="px-4 py-2 rounded-xl text-sm font-semibold bg-rose-500 text-white hover:bg-rose-600 transition-colors cursor-pointer"
          >
            Reintentar
          </button>
        </div>
      ) : (
        <CategoriaList
          categorias={categorias}
          onEdit={handleOpenEditModal}
          onDelete={handleDelete}
          deletingId={deletingId}
        />
      )}

      <CategoriaModal
        isOpen={isModalOpen}
        onClose={handleCloseModal}
        onSubmit={handleSubmitModal}
        categoriaEditar={categoriaEditar}
        isLoading={isSubmitting}
        errorMessage={modalError}
      />
    </div>
  );
}
