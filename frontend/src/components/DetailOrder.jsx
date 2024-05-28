import React from 'react'
import { useSelector } from 'react-redux'

const DetailOrder = () => {
    const detailOrder = useSelector(state => state.cart.cart)
    const handleChekout = (url_midtrans) =>{
      window.location.href = url_midtrans
    }
  return (
    <div>
        {detailOrder?<div>
            <h2>Detail Product</h2>
            <h5>Order ID          : {detailOrder.order_id}</h5>
            <h5>Produk            : {detailOrder.product}</h5>
            <h5>Harga             : {detailOrder.price}</h5>
            <h5>Jumlah            : {detailOrder.qty}</h5>
            <h5>Pembeli           : {detailOrder.customer_name}</h5>
            <h5>Email             : {detailOrder.email}</h5>
            <h5>No.Handphone      : {detailOrder.phone}</h5>
            <h5>Alamat            : {detailOrder.address}</h5>
        </div>:<></>}
        <button onClick={()=>handleChekout(detailOrder.url_midtrans)}>Checkout</button>
    </div>
  )
}

export default DetailOrder