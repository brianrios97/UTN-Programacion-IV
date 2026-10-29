import type { Table } from '@tanstack/react-table';

interface TablePaginationProps<TData> {
  table: Table<TData>;
}

export default function TablePagination<TData>({ table }: TablePaginationProps<TData>) {
  const pageIndex = table.getState().pagination.pageIndex;
  const pageCount = table.getPageCount();
  const totalRows = table.getPrePaginationRowModel().rows.length;

  return (
    <div className="flex flex-col sm:flex-row items-center justify-between gap-4 py-4 px-6 border-t border-slate-700/80 bg-slate-900/60 text-xs text-slate-400">
      <div>
        <span>Mostrando </span>
        <span className="font-semibold text-slate-200">
          {totalRows > 0 ? pageIndex * table.getState().pagination.pageSize + 1 : 0}
        </span>
        <span> a </span>
        <span className="font-semibold text-slate-200">
          {Math.min((pageIndex + 1) * table.getState().pagination.pageSize, totalRows)}
        </span>
        <span> de </span>
        <span className="font-semibold text-slate-200">{totalRows}</span>
        <span> registros</span>
      </div>

      <div className="flex items-center gap-2">
        <button
          onClick={() => table.previousPage()}
          disabled={!table.getCanPreviousPage()}
          className="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 text-slate-300 hover:text-white hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
        >
          Anterior
        </button>

        <span className="px-2 font-medium text-slate-300">
          Página {totalRows > 0 ? pageIndex + 1 : 0} de {Math.max(pageCount, 1)}
        </span>

        <button
          onClick={() => table.nextPage()}
          disabled={!table.getCanNextPage()}
          className="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 text-slate-300 hover:text-white hover:bg-slate-700 disabled:opacity-40 disabled:cursor-not-allowed transition-colors"
        >
          Siguiente
        </button>
      </div>
    </div>
  );
}
