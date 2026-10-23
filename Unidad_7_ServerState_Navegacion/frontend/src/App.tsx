import { Routes, Route, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import CategoriasPage from './pages/CategoriasPage';
import ProductsPage from './pages/ProductsPage';

function App() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col antialiased selection:bg-emerald-500 selection:text-white">
      <Navbar />
      <main className="flex-1">
        <Routes>
          <Route path="/" element={<Navigate to="/categorias" replace />} />
          <Route path="/categorias" element={<CategoriasPage />} />
          <Route path="/productos" element={<ProductsPage />} />
          <Route path="*" element={<Navigate to="/categorias" replace />} />
        </Routes>
      </main>
      <footer className="border-t border-slate-800/80 py-6 text-center text-xs text-slate-500 bg-slate-950/60">
        <p>Programaci?n IV ? Unidad 7: Server State &amp; Navegaci?n ? UTN TUPaD</p>
      </footer>
    </div>
  );
}

export default App;
