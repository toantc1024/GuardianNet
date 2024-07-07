"use client";
import React, { useCallback, useEffect, useState } from "react";
import { useConnection, useWallet } from "@solana/wallet-adapter-react";
import {
  Keypair,
  LAMPORTS_PER_SOL,
  SystemProgram,
  Transaction,
} from "@solana/web3.js";
import { Dialog, DialogContent, DialogTrigger } from "@/components/ui/dialog";
import Image from "next/image";
import { ChevronRight } from "lucide-react";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { WalletNotConnectedError } from "@solana/wallet-adapter-base";

//handle wallet balance fixed to 2 decimal numbers without rounding
export function toFixed(num: number, fixed: number): string {
  const re = new RegExp(`^-?\\d+(?:\\.\\d{0,${fixed || -1}})?`);
  return num.toString().match(re)![0];
}

import { Coin, Setting2 } from "iconsax-react";

import { ArrowDownOutlined, ArrowUpOutlined } from "@ant-design/icons";
import { Button, Card, Col, Row, Statistic } from "antd";
const Stats = () => <div className="h-full w-full px-4 bg-red-400">HE</div>;

import { Carousel } from "antd";
const contentStyle = {
  margin: 0,
  height: "300px",
  color: "#fff",
  lineHeight: "300px",
  textAlign: "center",
};
const DashboardCaroseul = ({ currentReward }: any) => {
  return (
    <div className="p-2 flex gap-2 flex-col">
      <Card bordered={false}>
        <Statistic
          title="Active"
          value={currentReward?.reward?.web_access || 0}
          precision={0}
          valueStyle={{ color: "#3f8600" }}
          prefix={<Coin />}
          suffix="rewards"
        />
      </Card>
    </div>
  );
};

const DashboardPage = ({ currentReward }: any) => {
  return (
    <>
      <DashboardCaroseul currentReward={currentReward} />
    </>
  );
};

const WalletConnection = () => {
  const { connection } = useConnection();
  const {
    select,
    wallets,
    publicKey,
    disconnect,
    connecting,
    sendTransaction,
  } = useWallet();

  const [open, setOpen] = useState<boolean>(false);
  const [balance, setBalance] = useState<number | null>(null);
  const [userWalletAddress, setUserWalletAddress] = useState<string>("");
  const onClick = useCallback(async () => {
    if (!publicKey) throw new WalletNotConnectedError();

    const transaction = new Transaction().add(
      SystemProgram.transfer({
        fromPubkey: publicKey,
        toPubkey: Keypair.generate().publicKey,
        lamports: 1_000_000,
      })
    );

    const signature = await sendTransaction(transaction, connection);

    await connection.confirmTransaction(signature, "processed");
  }, [publicKey, sendTransaction, connection]);

  useEffect(() => {
    if (!connection || !publicKey) {
      return;
    }

    connection.onAccountChange(
      publicKey,
      (updatedAccountInfo) => {
        setBalance(updatedAccountInfo.lamports / LAMPORTS_PER_SOL);
      },
      "confirmed"
    );

    connection.getAccountInfo(publicKey).then((info) => {
      if (info) {
        setBalance(info?.lamports / LAMPORTS_PER_SOL);
      }
    });
  }, [publicKey, connection]);

  useEffect(() => {
    setUserWalletAddress(publicKey?.toBase58()!);
  }, [publicKey]);

  const handleWalletSelect = async (walletName: any) => {
    if (walletName) {
      try {
        select(walletName);
        setOpen(false);
      } catch (error) {
        console.log("wallet connection err : ", error);
      }
    }
  };

  const currentUser = {
    user_id: "6689a18dd37c7380d03fda99",
    name: "fffff",
  };

  const [currentReward, setCurrentReward] = useState(0);
  useEffect(() => {
    (async () => {
      let response = await fetch(
        "http://localhost:8000/api/guardiannet/reward/" + currentUser.user_id,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      let data = await response.json();

      // .then((response) => response.json())
      // .then((data) => {
      //   setCurrentReward(data);
      // })
      // .catch((error) => {
      //   console.error("Error:", error);
      //   alert(error.message);
      // });
    })();
  }, []);

  const handleDisconnect = async () => {
    disconnect();
  };

  return (
    <div className="h-screen flex flex-col gap-4 w-full  items-center justify-center">
      <div className="">{publicKey?.toBase58()}</div>
      <DashboardPage currentReward={currentReward} />
      <Button onClick={onClick} disabled={!publicKey} className="primary">
        Widthdraw your reward
      </Button>
    </div>
  );
};

export default WalletConnection;
