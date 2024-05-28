import {createSlice, createAsyncThunk} from '@reduxjs/toolkit'

const initialState = {
    cart: null,
}

const cartSlice = createSlice({
    name: 'cart',
    initialState,
    reducers: {
        setCart: (state, actions) => {
            state.cart = actions.payload
        }
    },
})

export const {setCart} = cartSlice.actions;

export default cartSlice.reducer;