import { Link, NavLink, useLocation } from "react-router-dom";
import { logoInfo, menuItems } from "./Header.config";
import { useEffect, useState } from "react";

export const Header = () => {
  const location = useLocation();
  const [activeItem, setActiveItem] = useState("");

  useEffect(() => {
    setActiveItem(location.pathname);
  }, [location.pathname]);

  return (
    <header className="flex items-center justify-between">
      <Link to="/" className="h-[4.5rem]">
        <img
          src={logoInfo.src}
          alt={logoInfo.title}
          accessKey={logoInfo.title}
          className="h-full w-full invert"
        />
      </Link>
      <nav className="flex list-none" aria-label="Navigation Links Menu">
        {menuItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={`py-6 px-10 ${
              activeItem === item.path ? "bg-[#565C70]" : ""
            } hover:bg-[#697088]`}
          >
            <li>{item.name}</li>
          </NavLink>
        ))}
      </nav>
    </header>
  );
};
