import { createBrowserRouter } from "react-router-dom";
import { Layout } from "../layouts/Layout";
import { Dashboard } from "../pages/Dashboard";
import { InternalServerError } from "../pages/InternalServerError";
import { NotFound } from "../pages/NotFound";
import { Models } from "../pages/Models";

export const appRouter = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      {
        index: true,
        element: <Dashboard />,
        errorElement: <InternalServerError />,
      },
      {
        path: "models",
        element: <Models />,
      },
      {
        path: "*",
        element: <NotFound />,
      },
    ],
  },
]);
