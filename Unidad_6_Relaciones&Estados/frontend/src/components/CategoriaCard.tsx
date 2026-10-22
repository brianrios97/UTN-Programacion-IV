import type { Categoria } from '../types/categoria';

interface CategoriaCardProps {
  categoria: Categoria;
  index: number;
  onEdit: (categoria: Categoria) => void;
  onDelete: (id: number) => void;
}

export const CategoriaCard = ({
  categoria,
  index,
  onEdit,
  onDelete,
}: CategoriaCardProps) => {
  return (
    <tr className="border-b border-slate-800 hover:bg-slate-800/40 transition-colors">
      <td className="px-6 py-4 text-sm font-mono text-slate-400">
        {index + 1}
      </td>
      <td className="px-6 py-4 text-sm font-semibold text-white">
        {categoria.nombre}
      </td>
      <td className="px-6 py-4 text-sm text-slate-300 max-w-md">
        {categoria.descripcion}
      </td>
      <td className="px-6 py-4 text-right text-sm">
        <div className="flex items-center justify-end gap-2">
          <button
            onClick={() => onEdit(categoria)}
            className="px-3 py-1.5 bg-indigo-600/10 hover:bg-indigo-600/20 text-indigo-400 hover:text-indigo-300 text-xs font-semibold rounded-lg border border-indigo-500/30 transition-all cursor-pointer"
          >
            Editar
          </button>
          <button
            onClick={() => onDelete(categoria.id)}
            className="px-3 py-1.5 bg-rose-600/10 hover:bg-rose-600/20 text-rose-400 hover:text-rose-300 text-xs font-semibold rounded-lg border border-rose-500/30 transition-all cursor-pointer"
          >
            Eliminar
          </button>
        </div>
      </td>
    </tr>
  );
};
