import styled from 'styled-components';

export const Overlay = styled.div`
  position: absolute;
  top: 0;
  background: rgba(0, 0, 0, 0.7);
  width: 100%;
  height: 77.6rem;
  display: none;
  transition: 0.4s;
  
  ${({ sidebar }) =>
    sidebar &&
    `
		display: block;
		z-index: 4;	
	`}
`