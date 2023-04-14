import React from 'react'
import LayoutHeaderActionFullscreen from './HeaderActionFullscreen'
import LayoutHeaderActionToggleTheme from './HeaderActionToggleTheme'

const LayoutHeaderAction: React.FC = () => {
  return (
    <>
      <LayoutHeaderActionToggleTheme />
      <LayoutHeaderActionFullscreen />
    </>
  )
}

export default LayoutHeaderAction