import type { Categoria } from '../types/categoria';
import CategoriaCard from './CategoriaCard';

interface CategoriaListProps {
  categorias: Categoria[];
  onEdit: (categoria: Categoria) => void;
  onDelete: (id: number) => void;
  deletingId?: number | null;
}

export default function CategoriaList({
  categorias,
  onEdit,
  onDelete,
  deletingId = null,
}: CategoriaListProps) {
  if (categorias.length === 0) {
    return (
      <div className="text-center py-16 px-4 bg-slate-800/40 border border-dashed border-slate-700 rounded-3xl">
        <div className="w-16 h-16 mx-auto mb-4 rounded-2xl bg-slate-800 flex items-center justify-center text-slate-400">
          <svg className="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4" />
          </svg>
        </div>
        <h3 className="text-lg font-semibold text-slate-200 mb-1">No hay categor?as registradas</h3>
        <p className="text-sm text-slate-400 max-w-sm mx-auto">
          Comienza creando una nueva categor?a utilizando el bot?n superior.
        </p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {categorias.map((categoria) => (
        <CategoriaCard
          key={categoria.id}
          categoria={categoria}
          onEdit={onEdit}
          onDelete={onDelete}
          isDeleting={deletingId === categoria.id}
        />
      ))}
    </div>
  );
}
