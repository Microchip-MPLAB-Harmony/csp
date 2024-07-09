import ControlInterface from '../../Tools/ControlInterface';
declare const LoadDynamicComponents: (props: {
    componentId: string;
    dynamicSymbolsInfo: ControlInterface[];
    cx: (...classNames: string[]) => string;
<<<<<<< HEAD
}) => import("react/jsx-runtime").JSX.Element;
=======
}) => JSX.Element;
>>>>>>> 0d345d5887 (Added HTML clock manager PIC32CM_GC_SG supported devices)
export default LoadDynamicComponents;
