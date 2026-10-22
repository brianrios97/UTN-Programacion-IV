import { useEffect, useState } from 'react';
import { Navbar } from './components/Navbar';
import { CategoriaList } from './components/CategoriaList';
import { CategoriaModal } from './components/CategoriaModal';
import type { Categoria } from './types/categoria';

const API_URL = 'http://localhost:8000/categorias';

export function App() {
  const [categorias, setCategorias] = useState<Categoria[]>([]);
  const [isModalOpen, setIsModalOpen] = useState<boolean>(false);
  const [categoriaEditar, setCategoriaEditar] = useState<Categoria | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  // 1. useEffect: Carga inicial de datos al montar el componente
  useEffect(() => {
    fetchCategorias();
  }, []);

  const fetchCategorias = async () => {
    try {
      setLoading(true);
      setError(null);
      const res = await fetch(`${API_URL}/`);
      if (!res.ok) {
        throw new Error(`Error ${res.status}: No se pudieron cargar las categorías`);
      }
      const data: Categoria[] = await res.json();
      setCategorias(data);
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message);
      } else {
        setError('No se pudo conectar con el backend (asegurate de tenerlo iniciado en el puerto 8000)');
      }
    } finally {
      setLoading(false);
    }
  };

  // 2. Funciones para controlar apertura del modal
  const handleOpenCreate = () => {
    setCategoriaEditar(null);
    setIsModalOpen(true);
  };

  const handleOpenEdit = (categoria: Categoria) => {
    setCategoriaEditar(categoria);
    setIsModalOpen(true);
  };

  const handleCloseModal = () => {
    setIsModalOpen(false);
    setCategoriaEditar(null);
  };

  // 3. Función handleCreate con fetch nativo (POST)
  const handleCreate = async (nombre: string, descripcion: string) => {
    const res = await fetch(`${API_URL}/`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nombre, descripcion }),
    });

    if (res.status === 409) {
      const errorData = await res.json();
      throw new Error(errorData.detail || 'Ya existe una categoría con ese nombre.');
    }

    if (!res.ok) {
      throw new Error('Error al registrar la categoría.');
    }

    await fetchCategorias();
  };

  // 4. Función handleUpdate con fetch nativo (PUT)
  const handleUpdate = async (id: number, nombre: string, descripcion: string) => {
    const res = await fetch(`${API_URL}/${id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ nombre, descripcion }),
    });

    if (res.status === 409) {
      const errorData = await res.json();
      throw new Error(errorData.detail || 'Ya existe otra categoría con ese nombre.');
    }

    if (!res.ok) {
      throw new Error('Error al actualizar la categoría.');
    }

    await fetchCategorias();
  };

  // 5. Orquestador para guardar según si es creación o edición
  const handleSave = async (nombre: string, descripcion: string) => {
    if (categoriaEditar) {
      await handleUpdate(categoriaEditar.id, nombre, descripcion);
    } else {
      await handleCreate(nombre, descripcion);
    }
  };

  // 6. Función handleDelete con fetch nativo (DELETE)
  const handleDelete = async (id: number) => {
    const confirmacion = window.confirm(
      '¿Estás seguro de que deseas eliminar esta categoría? Se desvinculará de los productos asociados.'
    );
    if (!confirmacion) return;

    try {
      const res = await fetch(`${API_URL}/${id}`, {
        method: 'DELETE',
      });

      if (!res.ok) {
        throw new Error('No se pudo eliminar la categoría.');
      }

      await fetchCategorias();
    } catch (err: unknown) {
      alert(err instanceof Error ? err.message : 'Error al eliminar la categoría');
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col font-sans selection:bg-indigo-500 selection:text-white">
      {/* Barra de navegación superior */}
      <Navbar />

      {/* Contenido principal */}
      <main className="flex-1 max-w-6xl w-full mx-auto px-4 sm:px-6 py-8 sm:py-10">
        {/* Encabezado y botón de acción */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-8">
          <div>
            <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight flex items-center gap-3">
              Categorías
              <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-slate-800 text-indigo-400 border border-slate-700">
                {categorias.length}
              </span>
            </h1>
            <p className="text-slate-400 text-xs sm:text-sm mt-1">
              Administrá las categorías del catálogo en tiempo real con persistencia en base de datos.
            </p>
          </div>

          <button
            onClick={handleOpenCreate}
            className="inline-flex items-center justify-center gap-2 px-4 py-2.5 bg-indigo-600 hover:bg-indigo-500 text-white text-sm font-semibold rounded-xl shadow-lg hover:shadow-indigo-500/20 transition-all cursor-pointer self-start sm:self-auto"
          >
            <span className="text-base font-bold leading-none">+</span> Añadir Categoría
          </button>
        </div>

        {/* Mensaje de error de conexión */}
        {error && (
          <div className="mb-6 p-4 rounded-xl bg-rose-500/10 border border-rose-500/20 text-rose-300 text-sm flex items-center justify-between">
            <span>{error}</span>
            <button
              onClick={fetchCategorias}
              className="text-xs font-bold underline hover:text-white ml-4 cursor-pointer"
            >
              Reintentar
            </button>
          </div>
        )}

        {/* Estado de carga */}
        {loading ? (
          <div className="text-center py-20 bg-slate-900/40 rounded-2xl border border-slate-800/60">
            <div className="w-8 h-8 border-3 border-indigo-500 border-t-transparent rounded-full animate-spin mx-auto mb-3"></div>
            <p className="text-slate-400 text-sm font-medium">Cargando categorías desde la API...</p>
          </div>
        ) : (
          /* Listado de Categorías */
          <CategoriaList
            categorias={categorias}
            onEdit={handleOpenEdit}
            onDelete={handleDelete}
            onOpenCreateModal={handleOpenCreate}
          />
        )}
      </main>

      {/* Modal interactivo de Alta / Edición controlado por estado booleano */}
      <CategoriaModal
        isOpen={isModalOpen}
        categoriaEditar={categoriaEditar}
        onClose={handleCloseModal}
        onSubmit={handleSave}
      />
    </div>
  );
}

export default App;
