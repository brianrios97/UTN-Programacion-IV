import type { Categoria } from './categoria';

export interface Producto {
  id: number;
  nombre: string;
  descripcion: string;
  precio_base: number;
  imagenes_url: string[];
  disponible: boolean;
  activo?: boolean;
  categorias?: Categoria[];
}
