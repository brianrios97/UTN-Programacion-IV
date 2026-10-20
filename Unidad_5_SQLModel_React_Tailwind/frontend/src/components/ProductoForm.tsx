export const ProductoForm = () => {
  return (
    <div className="bg-slate-800/80 border border-slate-700/60 rounded-xl p-6 shadow-xl mb-10 max-w-2xl mx-auto">
      <div className="flex items-center gap-2 mb-4 border-b border-slate-700/60 pb-3">
        <div className="w-2.5 h-2.5 rounded-full bg-indigo-500"></div>
        <h2 className="text-lg font-bold text-white">Registrar Nuevo Producto</h2>
      </div>

      <form onSubmit={(e) => e.preventDefault()} className="space-y-4">
        <div>
          <label className="block text-xs font-semibold text-slate-300 mb-1">
            Nombre del Producto
          </label>
          <input
            type="text"
            placeholder="Ej: Teclado Mecánico RGB"
            className="w-full px-3.5 py-2 bg-slate-900/80 border border-slate-700 rounded-lg text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition-colors"
          />
        </div>

        <div>
          <label className="block text-xs font-semibold text-slate-300 mb-1">
            Descripción
          </label>
          <textarea
            rows={2}
            placeholder="Breve descripción de las características..."
            className="w-full px-3.5 py-2 bg-slate-900/80 border border-slate-700 rounded-lg text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition-colors resize-none"
          ></textarea>
        </div>

        <div>
          <label className="block text-xs font-semibold text-slate-300 mb-1">
            Precio ($)
          </label>
          <input
            type="number"
            placeholder="0.00"
            className="w-full px-3.5 py-2 bg-slate-900/80 border border-slate-700 rounded-lg text-sm text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 transition-colors"
          />
        </div>

        <button
          type="button"
          className="w-full py-2.5 px-4 bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm rounded-lg shadow-md hover:shadow-indigo-500/25 transition-all cursor-pointer"
        >
          Guardar Producto
        </button>
      </form>
    </div>
  );
};
