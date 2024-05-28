import ControlInterface from '../Tools/ControlInterface';
declare const LoadDynamicComponents: (props: {
    componentId: string;
    boxInfo: ControlInterface[];
    cx: (...classNames: string[]) => string;
}) => JSX.Element;
export default LoadDynamicComponents;
