import s from './Counter.module.scss'

export const Counter = () => {
	return (
		<div className='App'>
			<div>
				<h2>Счетчик:</h2>
				<h1>0</h1>
				<button className={s.minus}>- Минус</button>
				<button className={s.plus}>Плюс +</button>
			</div>
		</div>
	)
}
