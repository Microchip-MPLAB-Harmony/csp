import { Fieldset } from "primereact/fieldset";
import {createClassResolver} from "@mplab_harmony/harmony-plugin-client-lib";
import { FieldsetDetails, Symbols } from "./Summary";
import style from "./commonADCSummary.module.css";
const cx = createClassResolver(style);
type Props = {
  fieldsetDetails: FieldsetDetails[];
};
const CommonADCSummary = ({ fieldsetDetails }: Props) => {
  return (
    <div className={cx("summary-tab-container")}>
      {fieldsetDetails.map((symbolsData: FieldsetDetails) => (
        <Fieldset legend={symbolsData.fieldSetHeader}>
          {symbolsData.symbols.map((symbol: Symbols) => (
            <div className={cx("summary-options")}>
              <div>{symbol.label}</div>
              <div>{symbol.value}</div>
            </div>
          ))}
        </Fieldset>
      ))}
    </div>
  );
};

export default CommonADCSummary;
