# Frontend ? FoodStore UI (Unidad 8)

**Materia:** Programaci?n IV  
**Tecnicatura Universitaria en Programaci?n a Distancia ? UTN**  
**Estudiante:** Brian Emanuel Rios  

Frontend desarrollado con **React 19**, **TypeScript**, **TanStack Form**, **TanStack Table v8**, **TanStack Query v5** y **Tailwind CSS v4**.

---

## ?? Aspectos Implementados
1. **TanStack Table v8:**
   - Tablas interactivas en `CategoriasPage`, `ProductsPage` e `IngredientesPage`.
   - Columnas tipadas con `createColumnHelper`.
   - Ordenamiento multidireccional ascendente/descendente con `getSortedRowModel()`.
   - Paginaci?n cliente con `getPaginationRowModel()` y controles reutilizables en `TablePagination.tsx`.
2. **TanStack Form:**
   - Formularios modales tipados con `useForm` y componentes `form.Field`.
   - Validaciones por campo y por evento (`onChange`, `onBlur`).
   - Prevenci?n de env?os inv?lidos y visualizaci?n de errores contextuales.
3. **TanStack Query:**
   - `useQuery` para obtener y cachear el Server State.
   - `useMutation` con invalidaci?n autom?tica mediante `queryClient.invalidateQueries` tras cada alta, edici?n o baja.
4. **React Router:**
   - Rutas `/categorias`, `/productos` e `/ingredientes`.
   - `App.tsx` libre de l?gica de negocio o llamadas a la API.
