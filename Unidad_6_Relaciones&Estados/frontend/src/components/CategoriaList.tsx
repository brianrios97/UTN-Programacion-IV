import type { Categoria } from '../types/categoria';
import { CategoriaCard } from './CategoriaCard';

interface CategoriaListProps {
  categorias: Categoria[];
  onEdit: (categoria: Categoria) => void;
  onDelete: (id: number) => void;
  onOpenCreateModal: () => void;
}

export const CategoriaList = ({
  categorias,
  onEdit,
  onDelete,
  onOpenCreateModal,
}: CategoriaListProps) => {
  if (categorias.length === 0) {
    return (
      <div className="text-center py-16 px-4 bg-slate-900/60 rounded-2xl border border-slate-800 shadow-xl">
        <div className="w-16 h-16 rounded-full bg-slate-800 text-slate-400 flex items-center justify-center mx-auto mb-4 text-2xl font-bold">
          📁
        </div>
        <h3 className="text-lg font-bold text-white mb-1">
          No hay categorías registradas
        </h3>
        <p className="text-sm text-slate-400 max-w-sm mx-auto mb-6">
          Comenzá creando tu primera categoría para organizar los productos de la aplicación.
        </p>
        <button
          onClick={onOpenCreateModal}
          className="inline-flex items-center gap-2 px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold rounded-lg shadow-md transition-all cursor-pointer"
        >
          + Añadir Categoría
        </button>
      </div>
    );
  }

  return (
    <div className="bg-slate-900/80 rounded-2xl border border-slate-800 shadow-xl overflow-hidden">
      <div className="overflow-x-auto">
        <table className="w-full text-left border-collapse">
          <thead>
            <tr className="border-b border-slate-800 bg-slate-950/40 text-[11px] font-bold uppercase tracking-wider text-slate-400">
              <th className="px-6 py-4">NÚMERO</th>
              <th className="px-6 py-4">NOMBRE</th>
              <th className="px-6 py-4">DESCRIPCIÓN</th>
              <th className="px-6 py-4 text-right">ACCIONES</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800/60">
            {categorias.map((cat, index) => (
              <CategoriaCard
                key={cat.id}
                categoria={cat}
                index={index}
                onEdit={onEdit}
                onDelete={onDelete}
              />
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};
