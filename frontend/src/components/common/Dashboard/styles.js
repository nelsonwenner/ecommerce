import styled from 'styled-components';

export const Overlay = styled.div`
  margin-top: 0.7rem;
  position: absolute;
  top: 0;
  bottom:0;
  background: rgba(0, 0, 0, 0.7);
  width: 100%;
  height: 100%;
  display: none;
  transition: 0.4s;
  
  ${({ sidebar }) =>
    sidebar &&
    `
		display: block;
		z-index: 4;	
	`}
`