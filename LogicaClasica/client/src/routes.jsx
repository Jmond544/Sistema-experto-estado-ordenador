import { Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import About from "./pages/About";
import LogicaStandard from "./pages/LogicaStandard";
import Layout from "./pages/Layout";
import LogicaDifusa from "./pages/LogicaDifusa";

export default function ListRoutes() {
  return (
    <Routes>
      <Route path="/" element={<Layout />}>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
        <Route path="/logica-standard" element={<LogicaStandard />} />
        <Route path="/logica-difusa" element={<LogicaDifusa />} />
      </Route>
    </Routes>
  );
}
