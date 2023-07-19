import { FunctionalComponent, JSX } from "preact";
import './layout.css';

interface LayoutProps {
  children: JSX.Element;
}

const Layout: FunctionalComponent<LayoutProps> = ({ children }) => {
  return <main className='main'>{children}</main>;
};

export default Layout;
