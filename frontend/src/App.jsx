import { useState } from 'react'
import {BrowserRouter as Router, Routes, Route} from 'react-router-dom'
import Product from './components/Product'
import DetailOrder from './components/DetailOrder'
import Invoice from './components/Invoice'

function App() {

  return (
    <Router>
      <Routes>
        <Route path='/' element={<Product />} />
        <Route path='/orders' element={<DetailOrder />} />
        <Route path='/invoice' element={<Invoice />} />
      </Routes>
    </Router>
  )
}

export default App
