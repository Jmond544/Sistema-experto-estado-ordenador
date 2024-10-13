import { Link } from "react-router-dom";
import ButtonNavbar from "./ButtonNavbar";
import { GiDolphin } from "react-icons/gi";
export default function Navbar() {
  return (
    <nav className="fixed top-0 left-0 flex flex-row justify-between px-20 items-center py-4 border border-b-2 border-black/10 shadow-sm w-full backdrop-blur-md z-50">
      <Link to="/" className="flex flex-row items-center font-bold gap-2">
        <GiDolphin className="text-3xl" />
        <p className="flex flex-col text-center">
          <p>Grupo 03</p>
          <p className="text-xs">Sistemas inteligentes</p>
        </p>
      </Link>
      <ul className="flex flex-row gap-4">
        <li>
          <ButtonNavbar path="/" title="Home" />
        </li>
        <li>
          <ButtonNavbar path="/about" title="About" />
        </li>
        <li>
          <ButtonNavbar path="/logica-standard" title="Lógica Standard" />
        </li>
        <li>
          <ButtonNavbar path="/logica-difusa" title="Lógica Difusa" />
        </li>
      </ul>
    </nav>
  );
}
