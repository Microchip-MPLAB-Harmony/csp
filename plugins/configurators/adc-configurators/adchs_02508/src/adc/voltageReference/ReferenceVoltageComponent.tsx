import positions from "../../styles/positions.module.css";
import { DropDown, createClassResolver } from "@mplab_harmony/harmony-plugin-client-lib";
import ReferenceVoltage from "./ReferenceVoltage";
import useReferenceVoltageSymbols from "./useReferenceVoltageSymbols";

const cx = createClassResolver(positions);
const ReferenceVoltageComponent = () => {
  const { voltageReference } = useReferenceVoltageSymbols();
  return (
    <div>
      {/* <DropDown
        keyValueSetSymbolHook={voltageReference}
        className={cx("referenceVoltage")}
      ></DropDown> */}
      <ReferenceVoltage
        keyValueSetSymbolHook={voltageReference}
        classPrefix={"referenceVoltage"}
        classResolver={cx}
      />
      <label
        className={cx("avdd")}
        style={{
          fontWeight:
            voltageReference.value === 0 || voltageReference.value === 2
              ? "bold"
              : "initial",
        }}
      >
        AVDD
      </label>
      <label
        className={cx("vrefh")}
        style={{
          fontWeight:
            voltageReference.value === 1 || voltageReference.value === 3
              ? "bold"
              : "initial",
        }}
      >
        VREF+
      </label>
      <label
        className={cx("avss")}
        style={{
          fontWeight:
            voltageReference.value === 0 || voltageReference.value === 1
              ? "bold"
              : "initial",
        }}
      >
        {" "}
        AVSS
      </label>
      <label
        className={cx("vrefl")}
        style={{
          fontWeight:
            voltageReference.value === 2 || voltageReference.value === 3
              ? "bold"
              : "initial",
        }}
      >
        VREF-
      </label>
    </div>
  );
};

export default ReferenceVoltageComponent;
