import type { Categoria } from '../types/categoria';

interface CategoriaCardProps {
  categoria: Categoria;
  onEdit: (categoria: Categoria) => void;
  onDelete: (id: number) => void;
  isDeleting?: boolean;
}

export default function CategoriaCard({
  categoria,
  onEdit,
  onDelete,
  isDeleting = false,
}: CategoriaCardProps) {
  return (
    <div className="bg-slate-800/80 border border-slate-700/80 rounded-2xl p-6 shadow-lg shadow-black/20 hover:border-emerald-500/50 hover:shadow-emerald-500/10 transition-all duration-200 flex flex-col justify-between group">
      <div>
        <div className="flex items-center justify-between mb-3">
          <span className="px-2.5 py-1 text-xs font-semibold rounded-lg bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
            ID #{categoria.id}
          </span>
          <span className="w-2.5 h-2.5 rounded-full bg-emerald-400 group-hover:animate-ping" />
        </div>

        <h3 className="text-xl font-bold text-white mb-2 group-hover:text-emerald-300 transition-colors">
          {categoria.nombre}
        </h3>
        <p className="text-slate-300 text-sm leading-relaxed line-clamp-3">
          {categoria.descripcion || 'Sin descripci?n disponible.'}
        </p>
      </div>

      <div className="flex items-center gap-2 mt-6 pt-4 border-t border-slate-700/60">
        <button
          onClick={() => onEdit(categoria)}
          disabled={isDeleting}
          className="flex-1 px-3 py-2 text-sm font-medium rounded-xl bg-slate-700/60 hover:bg-slate-700 text-slate-200 hover:text-white transition-colors flex items-center justify-center gap-1.5 disabled:opacity-50 cursor-pointer"
        >
          <svg className="w-4 h-4 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
          </svg>
          Editar
        </button>

        <button
          onClick={() => onDelete(categoria.id)}
          disabled={isDeleting}
          className="px-3 py-2 text-sm font-medium rounded-xl bg-rose-500/10 hover:bg-rose-500/20 text-rose-300 hover:text-rose-200 border border-rose-500/20 transition-colors flex items-center justify-center gap-1.5 disabled:opacity-50 cursor-pointer"
        >
          {isDeleting ? (
            <svg className="w-4 h-4 animate-spin text-rose-400" fill="none" viewBox="0 0 24 24">
              <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
              <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z" />
            </svg>
          ) : (
            <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
            </svg>
          )}
          Eliminar
        </button>
      </div>
    </div>
  );
}
