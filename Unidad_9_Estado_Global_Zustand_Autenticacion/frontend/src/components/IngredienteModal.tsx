import { useEffect } from 'react';
import { useForm } from '@tanstack/react-form';
import type { Ingrediente } from '../types/ingrediente';

interface IngredienteModalProps {
  isOpen: boolean;
  onClose: () => void;
  onSubmit: (data: { nombre: string }) => void;
  ingredienteEditar: Ingrediente | null;
  isLoading: boolean;
  errorMessage?: string | null;
}

function FormContent({
  ingredienteEditar,
  onSubmit,
  onClose,
  isLoading,
  errorMessage,
}: Omit<IngredienteModalProps, 'isOpen'>) {
  const form = useForm({
    defaultValues: {
      nombre: ingredienteEditar?.nombre ?? '',
    },
    onSubmit: async ({ value }) => {
      onSubmit({
        nombre: value.nombre.trim(),
      });
    },
  });

  const isEditMode = Boolean(ingredienteEditar);

  return (
    <div
      className="bg-slate-900 border border-slate-700/80 rounded-3xl max-w-lg w-full p-6 sm:p-8 shadow-2xl relative overflow-hidden"
      onClick={(e) => e.stopPropagation()}
    >
      <div className="absolute top-0 left-0 right-0 h-1.5 bg-gradient-to-r from-emerald-500 via-teal-400 to-cyan-500" />

      <div className="flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-purple-500/10 border border-purple-500/20 flex items-center justify-center text-purple-400">
            <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z" />
            </svg>
          </div>
          <div>
            <h2 className="text-xl font-bold text-white">
              {isEditMode ? 'Editar Ingrediente' : 'Nuevo Ingrediente'}
            </h2>
            <p className="text-xs text-slate-400">
              Formulario gestionado con TanStack Form
            </p>
          </div>
        </div>

        <button
          onClick={onClose}
          disabled={isLoading}
          className="text-slate-400 hover:text-white p-2 rounded-xl hover:bg-slate-800 transition-colors disabled:opacity-50 cursor-pointer"
        >
          <svg className="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      </div>

      {errorMessage && (
        <div className="mb-4 p-3 rounded-xl bg-rose-500/10 border border-rose-500/30 text-rose-300 text-sm flex items-center gap-2">
          <svg className="w-4 h-4 shrink-0 text-rose-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
          </svg>
          <span>{errorMessage}</span>
        </div>
      )}

      <form
        onSubmit={(e) => {
          e.preventDefault();
          e.stopPropagation();
          form.handleSubmit();
        }}
        className="space-y-4"
      >
        <form.Field
          name="nombre"
          validators={{
            onChange: ({ value }) =>
              !value || !value.trim() ? 'El nombre del ingrediente es obligatorio' : undefined,
            onBlur: ({ value }) =>
              !value || !value.trim() ? 'El nombre del ingrediente es obligatorio' : undefined,
          }}
        >
          {(field) => (
            <div>
              <label htmlFor="ing-nombre" className="block text-sm font-medium text-slate-200 mb-1.5">
                Nombre del ingrediente <span className="text-emerald-400">*</span>
              </label>
              <input
                id="ing-nombre"
                name={field.name}
                value={field.state.value}
                onBlur={field.handleBlur}
                onChange={(e) => field.handleChange(e.target.value)}
                placeholder="Ej: Mozzarella, Albahaca, Gorgonzola"
                disabled={isLoading}
                className="w-full px-4 py-2.5 rounded-xl bg-slate-800/90 border border-slate-700 text-white placeholder-slate-500 focus:outline-none focus:border-emerald-500 focus:ring-1 focus:ring-emerald-500 transition-all text-sm disabled:opacity-60"
                autoFocus
              />
              {field.state.meta.errors.map((err) => (
                <p key={String(err)} className="text-rose-400 text-xs mt-1">
                  {String(err)}
                </p>
              ))}
            </div>
          )}
        </form.Field>

        <div className="flex items-center justify-end gap-3 pt-4 border-t border-slate-800 mt-6">
          <button
            type="button"
            onClick={onClose}
            disabled={isLoading}
            className="px-4 py-2.5 rounded-xl text-sm font-medium text-slate-300 hover:text-white hover:bg-slate-800 transition-colors disabled:opacity-50 cursor-pointer"
          >
            Cancelar
          </button>
          <button
            type="submit"
            disabled={isLoading}
            className="px-5 py-2.5 rounded-xl text-sm font-semibold text-white bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-600 hover:to-teal-600 shadow-lg shadow-emerald-500/25 transition-all flex items-center gap-2 disabled:opacity-50 cursor-pointer"
          >
            {isLoading ? (
              <>
                <svg className="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24">
                  <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                  <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z" />
                </svg>
                Guardando...
              </>
            ) : isEditMode ? (
              'Actualizar'
            ) : (
              'Guardar'
            )}
          </button>
        </div>
      </form>
    </div>
  );
}

export default function IngredienteModal(props: IngredienteModalProps) {
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && props.isOpen && !props.isLoading) {
        props.onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [props.isOpen, props.isLoading, props.onClose]);

  if (!props.isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/70 backdrop-blur-sm animate-fadeIn">
      <FormContent {...props} />
    </div>
  );
}
