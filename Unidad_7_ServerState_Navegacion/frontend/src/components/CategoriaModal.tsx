import { useState, useEffect } from 'react';
import type { Categoria } from '../types/categoria';

interface CategoriaModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSubmit: (data: { nombre: string; descripcion: string }) => void;
  categoriaEditar: Categoria | null;
  isLoading: boolean;
  errorMessage?: string | null;
}

export default function CategoriaModal({
  isOpen,
  onClose,
  onSubmit,
  categoriaEditar,
  isLoading,
  errorMessage = null,
}: CategoriaModalProps) {
  const [nombre, setNombre] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [validationError, setValidationError] = useState<string | null>(null);

  useEffect(() => {
    if (categoriaEditar) {
      setNombre(categoriaEditar.nombre);
      setDescripcion(categoriaEditar.descripcion || '');
    } else {
      setNombre('');
      setDescripcion('');
    }
    setValidationError(null);
  }, [categoriaEditar, isOpen]);

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && isOpen && !isLoading) {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [isOpen, isLoading, onClose]);

  if (!isOpen) return null;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!nombre.trim()) {
      setValidationError('El nombre de la categor?a es obligatorio.');
      return;
    }
    setValidationError(null);
    onSubmit({
      nombre: nombre.trim(),
      descripcion: descripcion.trim(),
    });
  };

  const isEditMode = Boolean(categoriaEditar);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm animate-fadeIn">
      <div
        className="bg-slate-900 border border-slate-700/80 rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-2xl relative overflow-hidden"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="absolute top-0 left-0 right-0 h-1.5 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-500" />

        <div className="flex items-center justify-between mb-6">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400">
              {isEditMode ? (
                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                </svg>
              ) : (
                <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 4v16m8-8H4" />
                </svg>
              )}
            </div>
            <div>
              <h2 className="text-xl font-bold text-white">
                {isEditMode ? 'Editar Categor?a' : 'Nueva Categor?a'}
              </h2>
              <p className="text-xs text-slate-400">
                {isEditMode
                  ? `Modificando la categor?a #${categoriaEditar?.id}`
                  : 'Ingresa los datos para registrar la categor?a'}
              </p>
            </div>
          </div>

          <button
            onClick={onClose}
            disabled={isLoading}
            className="text-slate-400 hover:text-white p-2 rounded-xl hover:bg-slate-800 transition-colors disabled:opacity-50 cursor-pointer"
          >
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {(validationError || errorMessage) && (
          <div className="mb-4 p-3 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-sm flex items-center gap-2">
            <svg className="w-4 h-4 shrink-0 text-rose-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span>{validationError || errorMessage}</span>
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label htmlFor="cat-nombre" className="block text-sm font-medium text-slate-200 mb-1.5">
              Nombre de la categor?a <span className="text-emerald-400">*</span>
            </label>
            <input
              id="cat-nombre"
              type="text"
              value={nombre}
              onChange={(e) => setNombre(e.target.value)}
              placeholder="Ej: Bebidas, Hamburguesas, Postres"
              disabled={isLoading}
              className="w-full px-4 py-2.5 rounded-xl bg-slate-800/90 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 transition-all text-sm disabled:opacity-60"
              autoFocus
            />
          </div>

          <div>
            <label htmlFor="cat-descripcion" className="block text-sm font-medium text-slate-200 mb-1.5">
              Descripci?n
            </label>
            <textarea
              id="cat-descripcion"
              value={descripcion}
              onChange={(e) => setDescripcion(e.target.value)}
              rows={3}
              placeholder="Breve detalle sobre los productos incluidos en esta categor?a..."
              disabled={isLoading}
              className="w-full px-4 py-2.5 rounded-xl bg-slate-800/90 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 transition-all text-sm resize-none disabled:opacity-60"
            />
          </div>

          <div className="flex items-center justify-end gap-3 pt-4 border-t border-slate-800 mt-6">
            <button
              type="button"
              onClick={onClose}
              disabled={isLoading}
              className="px-4 py-2.5 rounded-xl text-sm font-medium text-slate-300 hover:text-white hover:bg-slate-800 transition-colors disabled:opacity-50 cursor-pointer"
            >
              Cancelar
            </button>
            <button
              type="submit"
              disabled={isLoading}
              className="px-5 py-2.5 rounded-xl text-sm font-semibold text-white bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-600 hover:to-teal-600 shadow-lg shadow-emerald-500/25 transition-all flex items-center gap-2 disabled:opacity-50 cursor-pointer"
            >
              {isLoading ? (
                <>
                  <svg className="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z" />
                  </svg>
                  Guardando...
                </>
              ) : isEditMode ? (
                'Actualizar Categor?a'
              ) : (
                'Guardar Categor?a'
              )}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
