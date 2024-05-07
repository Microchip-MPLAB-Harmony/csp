import { useContext } from "react";
import {
  PluginConfigContext,
  useSymbols,
  ConfigSymbol,
  createClassResolver,
} from "@mplab_harmony/harmony-plugin-client-lib";
import useChannelSequencerSymbols from "../channelSequencer/useChannelSequencerSymbols";
import styles from "./dmaSequenceSummary.module.css";
import { DataTable } from "primereact/datatable";
import { Column } from "primereact/column";
const cx = createClassResolver(styles);
const DMASequenceSummary = () => {
  const { componentId = "adc" } = useContext(PluginConfigContext);
  const { isChannelSequencer, symbolIds } = useChannelSequencerSymbols();
  const symbols = useSymbols({ componentId, symbolIds }) as ConfigSymbol<any>[];
  const enabledSequencer: any = [];
  symbols.map((sequece) => {
    if (sequece?.value) {
      enabledSequencer.push({
        register: sequece?.label?.replace("Enable", ""),
        enable: sequece?.value,
      });
    }
    return 0;
  });
  return (
    <>
      {!isChannelSequencer.value ? (
        <div>Channel Sequencer Disabled</div>
      ) : (
        <DataTable value={enabledSequencer} tableStyle={{ minWidth: "10rem" }}>
          <Column
            field="register"
            header="Register"
            body={(e) => <div>{e?.register}</div>}
          ></Column>
          <Column
            field="enable"
            header="Enable"
            body={(e) => (
              <div style={{ textAlign: "center" }}>
                {e.register ? (
                  <i
                    className="pi pi-check"
                    style={{ color: "green", fontSize: "1.25rem" }}
                  ></i>
                ) : (
                  <i
                    className="pi pi-ban"
                    style={{ color: "orange", fontSize: "1.25rem" }}
                  ></i>
                )}
              </div>
            )}
          ></Column>
        </DataTable>
      )}
    </>
  );
};

export default DMASequenceSummary;
