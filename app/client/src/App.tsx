import { RouterProvider } from "react-router-dom";
import { appRouter } from "./routes/appRouter";
import "./App.css";

export const App = () => {
  return <RouterProvider router={appRouter} />;
};
