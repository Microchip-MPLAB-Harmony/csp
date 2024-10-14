import { SymbolProps } from '@mplab_harmony/harmony-plugin-client-lib';
export interface LabelProps {
    className: string;
    boldLabelStatus?: boolean;
    tooltip?: string;
    redColorForZeroFrequency?: boolean;
    minMaxOutofRangeRedColorStatus?: boolean;
}
declare const FrequencyLabelComponent: (props: SymbolProps & LabelProps) => import("react/jsx-runtime").JSX.Element;
export default FrequencyLabelComponent;
