import type { Producto } from '../types/producto';
import { ProductoCard } from './ProductoCard';

interface ProductoListProps {
  productos: Producto[];
}

export const ProductoList = ({ productos }: ProductoListProps) => {
  if (productos.length === 0) {
    return (
      <div className="text-center py-12 bg-slate-800/40 rounded-xl border border-slate-800">
        <p className="text-slate-400">No hay productos registrados en el catálogo.</p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {productos.map((prod) => (
        <ProductoCard key={prod.id} producto={prod} />
      ))}
    </div>
  );
};
