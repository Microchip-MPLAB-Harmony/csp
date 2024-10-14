import ControlInterface from '../../Tools/ControlInterface';
declare const LoadDynamicComponents: (props: {
    componentId: string;
    dynamicSymbolsInfo: ControlInterface[];
    cx: (...classNames: string[]) => string;
}) => import("react/jsx-runtime").JSX.Element;
export default LoadDynamicComponents;
