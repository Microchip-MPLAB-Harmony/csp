import { SymbolProps } from '@mplab_harmony/harmony-plugin-client-lib';
interface LabelProps {
    class: string;
    boldLabelStatus?: boolean;
    redColorForZeroFrequency?: boolean;
}
declare const FrequencyLabelComponent: (props: SymbolProps & LabelProps) => JSX.Element;
export default FrequencyLabelComponent;
