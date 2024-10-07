import { Link, useLocation } from "react-router-dom";

export default function ButtonNavbar({ path, title }) {
  const location = useLocation();
  const isActive = location.pathname === path;

  return (
    <Link
      to={path}
      className={`font-bold px-2 py-1 rounded-xl transition-all duration-300 border border-black border-opacity-0 ${
        isActive ? "bg-black text-white" : "hover:border-opacity-50"
      }`}
    >
      {title}
    </Link>
  );
}
