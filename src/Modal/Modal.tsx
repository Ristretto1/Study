import { useState } from 'react'
import s from './Modal.module.scss'

// Conditional Rendering
export const Modal = () => {
	const [isOpen, setIsOpen] = useState<boolean>(false)

	return (
		<div className='App'>
			<button className={s.open_modal_btn} onClick={() => setIsOpen(true)}>
				✨ Открыть окно
			</button>
			{isOpen && (
				<div className={s.overlay}>
					<div className={s.modal}>
						<div className={s.close_btn} onClick={() => setIsOpen(false)}>
							X
						</div>
						<img
							src={
								'https://media2.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif'
							}
						/>
					</div>
				</div>
			)}
		</div>
	)
}
