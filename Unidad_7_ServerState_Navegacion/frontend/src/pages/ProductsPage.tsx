export default function ProductsPage() {
  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <div className="pb-8 mb-8 border-b border-slate-800">
        <div className="flex items-center gap-3">
          <h1 className="text-3xl font-extrabold text-white tracking-tight">
            Cat?logo de Productos &amp; Relaciones N:N
          </h1>
          <span className="px-3 py-1 rounded-full text-xs font-semibold bg-teal-500/10 text-teal-400 border border-teal-500/20">
            Backend REST Client
          </span>
        </div>
        <p className="mt-1 text-sm text-slate-400 max-w-2xl">
          Arquitectura del paquete Cat?logo de Productos (UML FoodStore). Los endpoints del CRUD de productos y las asociaciones N:N con categor?as est?n implementados en FastAPI y se demuestran mediante REST Client.
        </p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 space-y-6">
          <div className="bg-slate-800/60 border border-slate-700 rounded-3xl p-6 sm:p-8">
            <h2 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
              <span className="w-8 h-8 rounded-lg bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400 text-sm font-mono">
                M
              </span>
              Entidad: Producto &amp; ProductoCategoria
            </h2>

            <p className="text-slate-300 text-sm mb-6 leading-relaxed">
              Cumpliendo las especificaciones del Trabajo Pr?ctico Integrador y el diagrama UML, el modelo de datos cuenta con validaciones de tipo Pydantic/SQLModel, persistencia de colecciones y relaci?n de muchos a muchos:
            </p>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-4">
                <span className="text-xs font-mono text-emerald-400 block mb-1">precio_base</span>
                <p className="text-white font-semibold text-sm">Validaci?n &gt;= 0</p>
                <p className="text-xs text-slate-400 mt-1">Field(ge=0) impide precios negativos en la API.</p>
              </div>

              <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-4">
                <span className="text-xs font-mono text-emerald-400 block mb-1">imagenes_url</span>
                <p className="text-white font-semibold text-sm">Array de Textos</p>
                <p className="text-xs text-slate-400 mt-1">Persistencia nativa PostgreSQL ARRAY / JSON en SQLite.</p>
              </div>

              <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-4">
                <span className="text-xs font-mono text-emerald-400 block mb-1">ProductoCategoria</span>
                <p className="text-white font-semibold text-sm">Tabla Intermedia N:N</p>
                <p className="text-xs text-slate-400 mt-1">PK compuesta (producto_id, categoria_id) + es_principal.</p>
              </div>

              <div className="bg-slate-900/80 border border-slate-800 rounded-2xl p-4">
                <span className="text-xs font-mono text-emerald-400 block mb-1">DELETE 204 No Content</span>
                <p className="text-white font-semibold text-sm">Respuesta HTTP 204</p>
                <p className="text-xs text-slate-400 mt-1">Eliminaci?n limpia y desvinculaci?n sin cascada hu?rfana.</p>
              </div>
            </div>
          </div>

          <div className="bg-slate-800/60 border border-slate-700 rounded-3xl p-6 sm:p-8">
            <h3 className="text-lg font-bold text-white mb-3">
              Endpoints Disponibles para Demostraci?n (.http)
            </h3>
            <div className="space-y-2 text-xs font-mono">
              <div className="flex items-center gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800">
                <span className="px-2 py-0.5 rounded bg-blue-500/10 text-blue-400 font-bold">GET</span>
                <span className="text-slate-300">/productos/</span>
                <span className="ml-auto text-slate-500">Listar productos con categor?as</span>
              </div>
              <div className="flex items-center gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800">
                <span className="px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 font-bold">POST</span>
                <span className="text-slate-300">/productos/</span>
                <span className="ml-auto text-slate-500">Crear producto (201 Created)</span>
              </div>
              <div className="flex items-center gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800">
                <span className="px-2 py-0.5 rounded bg-purple-500/10 text-purple-400 font-bold">POST</span>
                <span className="text-slate-300">/productos/&#123;id&#125;/categorias/&#123;cat_id&#125;</span>
                <span className="ml-auto text-slate-500">Vincular categor?a N:N</span>
              </div>
              <div className="flex items-center gap-2 p-2.5 rounded-xl bg-slate-900/80 border border-slate-800">
                <span className="px-2 py-0.5 rounded bg-rose-500/10 text-rose-400 font-bold">DELETE</span>
                <span className="text-slate-300">/productos/&#123;id&#125;</span>
                <span className="ml-auto text-slate-500">Baja l?gica/f?sica (204 No Content)</span>
              </div>
            </div>
          </div>
        </div>

        <div className="space-y-6">
          <div className="bg-gradient-to-br from-slate-800/80 to-slate-900/90 border border-slate-700 rounded-3xl p-6 shadow-xl">
            <h3 className="text-lg font-bold text-white mb-2 flex items-center gap-2">
              <svg className="w-5 h-5 text-emerald-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
              Demostraci?n REST Client
            </h3>
            <p className="text-slate-300 text-sm mb-4">
              En la carpeta del backend se encuentra el archivo listo para ejecutar peticiones HTTP directas en VS Code:
            </p>
            <div className="p-3 bg-slate-950 rounded-xl border border-slate-800 font-mono text-xs text-emerald-400 mb-4 break-all">
              backend/productos.http
            </div>
            <ul className="text-xs text-slate-400 space-y-2 mb-4 list-disc list-inside">
              <li>Abrir con la extensi?n REST Client.</li>
              <li>Hacer clic en &quot;Send Request&quot; en cada bloque.</li>
              <li>Comprueba altas, consultas, relaciones N:N y errores 404/409/422.</li>
            </ul>
            <a
              href="http://localhost:8000/docs"
              target="_blank"
              rel="noreferrer"
              className="inline-flex items-center justify-center w-full px-4 py-2.5 rounded-xl text-sm font-semibold text-emerald-400 bg-emerald-500/10 hover:bg-emerald-500/20 border border-emerald-500/20 transition-colors gap-2"
            >
              <span>Abrir Swagger UI (/docs)</span>
              <svg className="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
              </svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}
