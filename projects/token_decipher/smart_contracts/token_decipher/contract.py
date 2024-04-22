from algopy import ARC4Contract, String, arc4, itxn


class TokenDecipher(ARC4Contract):

    asset_name: String
    unit_name: String

    @arc4.abimethod(allow_actions=["NoOp"],create="require")
    def createApplication(self, assetName:String, uintName:String) -> None:     # noqa: N802, N803
        self.asset_name = assetName
        self.uint_name = uintName

    @arc4.abimethod()
    def createAsset(self) ->None:                                                 # noqa: N802
        self.asset_created = (
            itxn.AssetConfig(
            asset_name= self.asset_name,
            unit_name=self.unit_name,
            total= 1000,
            decimals= 1,
            default_frozen=False
        )
        .submit()
        .created_asset.id
        )

