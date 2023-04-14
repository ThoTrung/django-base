import React from 'react'
import { Button, useTheme } from '@blueupcode/components'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faSun, faMoon } from '@fortawesome/free-solid-svg-icons'

const LayoutHeaderActionToggleTheme: React.FC = () => {
	const { resolvedTheme: theme, setTheme } = useTheme()

	const handleToggleTheme = () => {
		if (theme === 'dark') {
			setTheme('light')
		} else {
			setTheme('dark')
		}
	}

	return (
			<Button icon variant="flat-primary" onClick={handleToggleTheme}>
				{theme && <FontAwesomeIcon icon={theme === 'dark' ? faSun : faMoon} />}
			</Button>
	)
}

export default LayoutHeaderActionToggleTheme
