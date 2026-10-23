import { Routes, Route, Navigate } from 'react-router-dom';
import Navbar from './components/Navbar';
import CategoriasPage from './pages/CategoriasPage';
import ProductsPage from './pages/ProductsPage';
import IngredientesPage from './pages/IngredientesPage';

function App() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col antialiased selection:bg-emerald-500 selection:text-white">
      <Navbar />
      <main className="flex-1">
        <Routes>
          <Route path="/" element={<Navigate to="/categories" replace />} />
          {/* Rutas requeridas por la consigna (/categories, /products, /ingredients) */}
          <Route path="/categories" element={<CategoriasPage />} />
          <Route path="/products" element={<ProductsPage />} />
          <Route path="/ingredients" element={<IngredientesPage />} />
          
          {/* Alias en espa?ol para m?xima compatibilidad */}
          <Route path="/categorias" element={<CategoriasPage />} />
          <Route path="/productos" element={<ProductsPage />} />
          <Route path="/ingredientes" element={<IngredientesPage />} />
          
          <Route path="*" element={<Navigate to="/categories" replace />} />
        </Routes>
      </main>
      <footer className="border-t border-slate-800/80 py-6 text-center text-xs text-slate-500 bg-slate-950/60">
        <p>Programacion IV - Unidad 8: Formularios &amp; Tablas (TanStack Form &amp; Table v8) - UTN TUPaD</p>
      </footer>
    </div>
  );
}

export default App;
