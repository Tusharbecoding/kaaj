import React from "react";

function ResultsTable({ data }) {
  if (!data || data.length === 0) {
    return <p className="text-gray-600 text-center">No results found.</p>;
  }

  return (
    <div className="overflow-x-auto">
      <table className="min-w-full bg-white border border-gray-200 rounded-lg shadow-sm">
        <thead>
          <tr className="bg-gray-100 text-gray-700 uppercase text-sm leading-normal">
            <th className="py-3 px-6 text-left">Business Name</th>
            <th className="py-3 px-6 text-left">Document Number</th>
            <th className="py-3 px-6 text-left">Status</th>
          </tr>
        </thead>
        <tbody className="text-gray-600 text-sm font-light">
          {data.map((item, index) => (
            <tr
              key={index}
              className="border-b border-gray-200 hover:bg-gray-100"
            >
              <td className="py-3 px-6">{item.business_name || "N/A"}</td>
              <td className="py-3 px-6">{item.doc_number || "N/A"}</td>
              <td className="py-3 px-6">{item.status || "N/A"}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ResultsTable;
