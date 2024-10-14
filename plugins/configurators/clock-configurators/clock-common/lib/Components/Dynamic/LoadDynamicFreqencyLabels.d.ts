import ControlInterface from '../../Tools/ControlInterface';
declare const LoadDynamicFreqencyLabels: (props: {
    componentId: string;
    dynamicLabelSymbolsInfo: ControlInterface[];
    cx: (...classNames: string[]) => string;
    boldLabelStatus?: boolean | undefined;
    toolTip?: string | undefined;
    redColorForZeroFrequency?: boolean | undefined;
}) => import("react/jsx-runtime").JSX.Element;
export default LoadDynamicFreqencyLabels;
