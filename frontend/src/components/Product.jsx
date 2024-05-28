import React, { useState } from 'react'
import axios from 'axios'
import { useDispatch } from 'react-redux';
import { setCart } from '../reducers/cartReducer';
import { Link } from 'react-router-dom';

const Product = () => {
    const dispatch = useDispatch()

    const handlePlaceOrder = async () => {

        const data = {
            product: 'Headset',
            price: 55000,
            qty: 1,
            customer_name: 'Zulfan Rohim',
            email: 'rohim@gmail.com',
            phone: '082365598965',
            address: 'Dk.Gardu, Buniwah, Kec.Sirampog, Kab.Brebes, Jawa Tengah'
        }

        try {
            const response = await axios.post('http://localhost:8000/api/orders/', data);
            dispatch(setCart(response.data))
        } catch (error) {
            console.error('Error placing order', error);
        }
    };

    return (
        <div>
            <Link to='/orders'>
                <button onClick={handlePlaceOrder}>Beli</button>
            </Link>
        </div>
    );
}

export default Product