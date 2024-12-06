import { Outlet } from "react-router-dom";
import { Header } from "../containers/Header";

export const Layout = () => {
  return (
    <>
      <div className="bg-[#191C24] text-[#EEF3FF] px-10">
        <Header />
      </div>
      <div className="bg-[#303545] text-[#EEF3FF] px-10">
        <Outlet />
      </div>
    </>
  );
};
