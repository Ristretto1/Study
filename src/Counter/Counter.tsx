import { useState } from 'react'
import s from './Counter.module.scss'

export const Counter = () => {
	const [count, setCount] = useState(0)

	const plus = () => {
		setCount(state => state + 1)
	}
	const minus = () => {
		setCount(state => state - 1)
	}

	return (
		<div className='App'>
			<div>
				<h2>Счетчик:</h2>
				<h1>{count}</h1>
				<button className={s.minus} onClick={minus}>
					- Минус
				</button>
				<button className={s.plus} onClick={plus}>
					Плюс +
				</button>
			</div>
		</div>
	)
}
