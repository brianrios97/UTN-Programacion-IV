import { Navbar } from './components/Navbar';
import { Footer } from './components/Footer';
import { ProductoForm } from './components/ProductoForm';
import { ProductoList } from './components/ProductoList';
import type { Producto } from './types/producto';

// Al menos 3 productos hardcodeados requeridos por HU-04
const PRODUCTOS_INICIALES: Producto[] = [
  {
    id: 1,
    nombre: 'Teclado Mecánico RGB Pro',
    descripcion: 'Switches mecánicos blue táctiles con retroiluminación RGB por tecla y chasis de aluminio.',
    precio: 45000,
  },
  {
    id: 2,
    nombre: 'Mouse Gamer Ergonómico 16000 DPI',
    descripcion: 'Sensor óptico de alta precisión con 6 botones programables y pesas ajustables.',
    precio: 28500,
  },
  {
    id: 3,
    nombre: 'Monitor Curvo 27" 144Hz Full HD',
    descripcion: 'Panel VA antirreflejo con 1ms de tiempo de respuesta y soporte FreeSync Premium.',
    precio: 195000,
  },
  {
    id: 4,
    nombre: 'Auriculares Inalámbricos 7.1 Surround',
    descripcion: 'Cancelación activa de ruido, almohadillas memory foam y micrófono retráctil.',
    precio: 62000,
  },
];

export function App() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-sans selection:bg-indigo-500 selection:text-white">
      {/* 1. Barra de Navegación */}
      <Navbar />

      {/* Contenido Principal */}
      <main className="flex-1 max-w-6xl w-full mx-auto px-4 py-8">
        {/* Encabezado */}
        <div className="text-center mb-10">
          <span className="text-xs font-semibold uppercase tracking-wider text-indigo-400 bg-indigo-500/10 px-3 py-1 rounded-full border border-indigo-500/20">
            Gestor de Catálogo
          </span>
          <h1 className="text-3xl sm:text-4xl font-extrabold text-white mt-3 mb-2 tracking-tight">
            Catálogo de Productos
          </h1>
          <p className="text-slate-400 text-sm max-w-lg mx-auto">
            Interfaz moderna maquetada con React, TypeScript y Tailwind CSS en componentes funcionales puros.
          </p>
        </div>

        {/* 2. Formulario de Alta */}
        <ProductoForm />

        {/* 3. Listado de Productos */}
        <section className="mt-8">
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-xl font-bold text-white flex items-center gap-2">
              Productos Disponibles
              <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-slate-800 text-indigo-300 border border-slate-700">
                {PRODUCTOS_INICIALES.length}
              </span>
            </h2>
          </div>

          <ProductoList productos={PRODUCTOS_INICIALES} />
        </section>
      </main>

      {/* 4. Pie de página */}
      <Footer />
    </div>
  );
}

export default App;
