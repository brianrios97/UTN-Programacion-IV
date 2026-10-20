import type { Producto } from '../types/producto';

interface ProductoCardProps {
  producto: Producto;
}

export const ProductoCard = ({ producto }: ProductoCardProps) => {
  return (
    <div className="bg-slate-800/80 border border-slate-700/60 rounded-xl p-5 shadow-lg hover:shadow-indigo-500/10 hover:border-indigo-500/50 transition-all duration-300 flex flex-col justify-between group">
      <div>
        <div className="flex justify-between items-start gap-2 mb-3">
          <span className="text-xs font-mono font-semibold px-2 py-0.5 rounded bg-slate-700 text-indigo-300">
            #{producto.id}
          </span>
          <span className="text-xs font-medium px-2.5 py-0.5 rounded-full bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
            Disponible
          </span>
        </div>

        <h3 className="text-lg font-bold text-white group-hover:text-indigo-400 transition-colors">
          {producto.nombre}
        </h3>

        <p className="text-sm text-slate-400 mt-2 line-clamp-2">
          {producto.descripcion}
        </p>
      </div>

      <div className="mt-5 pt-4 border-t border-slate-700/60 flex items-center justify-between">
        <div>
          <span className="text-xs text-slate-400 block">Precio</span>
          <span className="text-xl font-extrabold text-white">
            ${producto.precio.toLocaleString('es-AR')}
          </span>
        </div>
        <button className="px-3.5 py-1.5 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold rounded-lg shadow-sm transition-colors cursor-pointer">
          Ver detalle
        </button>
      </div>
    </div>
  );
};
