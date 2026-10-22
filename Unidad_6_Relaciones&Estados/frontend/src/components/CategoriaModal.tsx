import { useEffect, useState } from 'react';
import type { Categoria } from '../types/categoria';

interface CategoriaModalProps {
  isOpen: boolean;
  categoriaEditar: Categoria | null;
  onClose: () => void;
  onSubmit: (nombre: string, descripcion: string) => Promise<void>;
}

export const CategoriaModal = ({
  isOpen,
  categoriaEditar,
  onClose,
  onSubmit,
}: CategoriaModalProps) => {
  const [nombre, setNombre] = useState('');
  const [descripcion, setDescripcion] = useState('');
  const [guardando, setGuardando] = useState(false);
  const [errorLocal, setErrorLocal] = useState<string | null>(null);

  // Sincronizar estado cuando se abre para editar o para crear
  useEffect(() => {
    if (categoriaEditar) {
      setNombre(categoriaEditar.nombre);
      setDescripcion(categoriaEditar.descripcion);
    } else {
      setNombre('');
      setDescripcion('');
    }
    setErrorLocal(null);
  }, [categoriaEditar, isOpen]);

  if (!isOpen) return null;

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!nombre.trim()) {
      setErrorLocal('El nombre de la categoría es obligatorio.');
      return;
    }
    try {
      setGuardando(true);
      setErrorLocal(null);
      await onSubmit(nombre.trim(), descripcion.trim());
      onClose();
    } catch (err: unknown) {
      if (err instanceof Error) {
        setErrorLocal(err.message);
      } else {
        setErrorLocal('Ocurrió un error inesperado al guardar.');
      }
    } finally {
      setGuardando(false);
    }
  };

  const isEditing = Boolean(categoriaEditar);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/70 backdrop-blur-sm transition-opacity">
      <div className="bg-slate-900 border border-slate-700/80 rounded-2xl p-6 sm:p-7 w-full max-w-md shadow-2xl animate-in fade-in zoom-in-95 duration-200">
        <div className="flex items-center justify-between pb-4 border-b border-slate-800 mb-5">
          <h3 className="text-lg font-bold text-white tracking-tight">
            {isEditing ? 'Editar Categoría' : 'Añadir Categoría'}
          </h3>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-white p-1 rounded-lg hover:bg-slate-800 transition-colors"
          >
            ✕
          </button>
        </div>

        {errorLocal && (
          <div className="mb-4 p-3 rounded-lg bg-rose-500/10 border border-rose-500/30 text-rose-400 text-xs font-medium">
            {errorLocal}
          </div>
        )}

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-xs font-semibold text-slate-300 mb-1.5">
              Nombre de la categoría
            </label>
            <input
              type="text"
              value={nombre}
              onChange={(e) => setNombre(e.target.value)}
              placeholder="Ej: Pizzas, Bebidas, etc."
              autoFocus
              className="w-full px-3.5 py-2.5 bg-slate-950/70 border border-slate-700 rounded-xl text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-colors"
            />
          </div>

          <div>
            <label className="block text-xs font-semibold text-slate-300 mb-1.5">
              Descripción
            </label>
            <textarea
              rows={3}
              value={descripcion}
              onChange={(e) => setDescripcion(e.target.value)}
              placeholder="Breve detalle de los productos que agrupa..."
              className="w-full px-3.5 py-2.5 bg-slate-950/70 border border-slate-700 rounded-xl text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500 transition-colors resize-none"
            ></textarea>
          </div>

          <div className="flex items-center justify-end gap-3 pt-3 border-t border-slate-800/80">
            <button
              type="button"
              onClick={onClose}
              disabled={guardando}
              className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white text-xs font-semibold rounded-lg border border-slate-700 transition-colors cursor-pointer"
            >
              Cancelar
            </button>
            <button
              type="submit"
              disabled={guardando}
              className="px-5 py-2 bg-indigo-600 hover:bg-indigo-500 disabled:opacity-50 text-white text-xs font-semibold rounded-lg shadow-md hover:shadow-indigo-500/20 transition-all cursor-pointer"
            >
              {guardando ? 'Guardando...' : 'Guardar'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};
