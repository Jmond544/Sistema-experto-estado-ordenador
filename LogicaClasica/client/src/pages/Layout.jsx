import Navbar from "../components/Navbar";
import { Outlet } from "react-router-dom";

export default function Layout() {
  return (
    <div className="relative">
      <Navbar />
      <div className="mx-20">
      <Outlet />
      </div>
    </div>
  );
}
