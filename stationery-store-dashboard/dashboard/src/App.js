import { BrowserRouter, Route, Routes } from 'react-router-dom';

import './App.css';
import Header from './components/Header';
import Commissions from './pages/Commissions';
import Sales from './pages/Sales';

function App() {
  return (
    <>
      <BrowserRouter>
        <Header/>
        <Routes>
          <Route path='/' element={<Sales/>} />
          <Route path='/vendas' element={<Sales/>} />
          <Route path='/comissoes' element={<Commissions/>} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;