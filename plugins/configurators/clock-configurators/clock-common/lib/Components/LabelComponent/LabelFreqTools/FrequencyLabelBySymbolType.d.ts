import { SymbolProps } from '@mplab_harmony/harmony-plugin-client-lib';
import { LabelProps } from '../FrequencyLabelComponent';
interface LabelNewProps extends LabelProps {
    symbolType: string;
}
declare const FrequencyLabelBySymbolType: (props: SymbolProps & LabelNewProps) => import("react/jsx-runtime").JSX.Element | null;
export default FrequencyLabelBySymbolType;
